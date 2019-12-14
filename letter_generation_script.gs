function myFunction() {
  
function myFunction() {
 
  var templateId = '1OmJRSiuAPC0KIl2S_XPRdw7wCXotTdmyT3NiFCBlolU'; 
  var ui = DocumentApp.getUi();
  var spreadsheetName = ui.prompt('Enter name of contact spreadsheet');
 
  //Get the information from the spreadsheet   
  var spreadId = DriveApp.getFileById(spreadsheet_id).makeCopy().getId();

  //Make a copy of the template file
  var documentId = DriveApp.getFileById(template_id).makeCopy().getId();
      
  //Rename the copied file
  DriveApp.getFileById(documentId).setName(nameResponse.getResponseText() + date + ' Sales Report');  
      
  //Get the document body as a variable
  var body = DocumentApp.openById(documentId).getBody();
    
  //Insert the entries into the document
  body.replaceText('##DONOR_NAME##', donor_name);
  body.replaceText('##DONATION_AMOUNT##', amount);
  body.replaceText('##LETTER_BODY##', letter_body); 
}








