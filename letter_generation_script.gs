// 1. Prompt for contacts file name, url of letter template
// 2. Populate google spreadsheet with necessary contact info for letters
// 3. Create folder for letters
// 4. Read letter info from spreadsheet
// 5. Generate letters from info and template, place them in folder letter

function userInput() {

  var ui = DocumentApp.getUi();
  var spreadsheetUrl = ui.prompt('Enter URL of contact spreadsheet');
  var templateUrl = ui.prompt('Enter URL of template') 
  var sprdsheet = SpreadsheetApp.openByUrl(spreadsheetUrl);
  var tmplate = DriveApp.openByUrl(templateUrl);
  var input = {template: tmplate, spreadsheet: sprdsheet};
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
  var firstNameIndex = data[0].indexOf('First');
  var lastNameIndex = data[0].indexOf('Last');
  var zipCodeIndex = data[0].indexOf('Zip');
  var addressIndex = data[0].indexOf('Address');
  var cityIndex = data[0].indexOf('City');
  var stateIndex = data[0].indexOf('State');
  var donationIndex = data[0].indexOf('Donation');
  var contactArray = [];

  for (var i = 0; i < data.length; i++) {
    var frst = data[i][firstNameIndex];
    var lst = data[i][lastNameIndex];
    var zp = data[i][zipCodeIndex];
    var addrss = data[i][addressIndex];
    var cty = data[i][cityIndex]
    var stte = data[i][stateIndex]
    var dnation = data[i][donationIndex]
    var contact = {FirstName: frst, LastName: lst, ZipCode: zp, Address: addrss, City: cty, State: stte, Donation: dnation}
    contactArray.push(contact);
  } 

  return contactArray;
}


function makeLetter(templateId, date, contact) { 

  //Make a copy of the template file
  var documentId = DriveApp.getFileById(templateId).makeCopy().getId();
  var donorName = contact.FirstName + " " + contact.LastName;
  var letterName = date + "_" + donorName;
 
  //Rename the copied file
  DriveApp.getFileById(documentId).setName(letterName);
      
  //Get the document body as a variable
  var body = DocumentApp.openById(documentId).getBody();
  
  //Insert the entries into the document
  body.replaceText('##DONOR_NAME##', donorName);
  body.replaceText('##DONATION_AMOUNT##', contact.Donation);
}

//Start with file upload of contact csv, a few more inputs, then get all the letters and address labels
function writeDonorLetters() {
 
 

}










