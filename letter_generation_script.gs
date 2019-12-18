// 1. Prompt for contacts file name, url of letter template
// 2. Populate google spreadsheet with necessary contact info for letters
// 3. Create folder for letters
// 4. Read letter info from spreadsheet
// 5. Generate letters from info and template, place them in folder letter

function userInput() {

  var ui = DocumentApp.getUi();
  var spreadsheetUrl = ui.prompt('Enter URL of contact spreadsheet');
  var templateUrl = ui.prompt('Enter URL of template') 
  var flderName = ui.prompt('Enter name for folder to put letters') 
  var dte = ui.prompt('Enter date to put on letters') 
  var sprdsheet = SpreadsheetApp.openByUrl(spreadsheetUrl);
  var tmplate = DriveApp.openByUrl(templateUrl);
  var input = {template: tmplate, spreadsheet: sprdsheet, folderName: flderName, date: dte};
  return input;
}

function createLetterFolder(folderName) {

  var thisFileId = DriveApp.getActive().getId();
  var thisFile = DriveApp.getFileById(thisFileId);
  var parentFolder = thisFile.getParents()[0].getName();
  var parentFolder=DriveApp.getFolderById(parentFolderId);
  var newFolder=parentFolder.createFolder(folderName);
  return newFolder;
} 

function loadSpreadsheet(sheet) {
  var data = sheet.getDataRange().getValues();
  var firstNameIndex = data[0].indexOf('First Name');
  var lastNameIndex = data[0].indexOf('Last Name');
  var zipCodeIndex = data[0].indexOf('Home Zip5');
  var addressIndex = data[0].indexOf('Home Address');
  var cityIndex = data[0].indexOf('Home City');
  var stateIndex = data[0].indexOf('Home State');
  var contactArray = [];

  for (var i = 0; i < data.length; i++) {
    var frst = data[i][firstNameIndex];
    var lst = data[i][lastNameIndex];
    var zp = data[i][zipCodeIndex];
    var addrss = data[i][addressIndex];
    var cty = data[i][cityIndex];
    var stte = data[i][stateIndex];
    var contact = {FirstName: frst, LastName: lst, ZipCode: zp, Address: addrss, City: cty, State: stte}; 
    contactArray.push(contact);
  } 

  return contactArray;
}

function move_file(file_id, target_folder_id) {
  var source_file = DriveApp.getFileById(file_id);
  var source_folder = source_file.getParents().next();
  if (source_folder.getId() != target_folder_id) {
    DriveApp.getFolderById(target_folder_id).addFile(source_file);
    source_folder.removeFile(source_file);
  }
}

function makeLetter(templateId, date, contact, folder) { 

  //Make a copy of the template file
  var documentId = DriveApp.getFileById(templateId).makeCopy().getId();
  var letterName = date + "_" + donorName;
 
  //Rename the copied file
  var letterFileId = DriveApp.getFileById(documentId);  
  
  DriveApp.getFileById(documentId).setName(letterName);
  move_file(documentId, folder);
    
  //Get the document body as a variable
  var body = DocumentApp.openById(documentId).getBody();
  
  //Insert the entries into the document
  body.replaceText('##FIRSTNAME##', contact.FirstName);
  body.replaceText('##LASTNAME##', contact.LastName);
  body.replaceText('##ADDRESS##', contact.Address);
  body.replaceText('##CITY##', contact.City);
  body.replaceText('##STATE##', contact.State);
  body.replaceText('##ZIP##', contact.ZipCode);
}

//Start with file upload of contact csv, a few more inputs, then get all the letters and address labels
function writeDonorLetters() {
  var input = userInput();
  var contactArray = loadSpreadsheet(input.spreadSheet);
  var folder = createLetterFolder(input.folderName);
  for (var i = 0; i < contactArray.length; i++) {
    contact = contactArray[i];
    makeLetter(input.template, input.date, contact, folder); 
  }
}










