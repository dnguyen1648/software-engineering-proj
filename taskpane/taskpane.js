
/* global document, Office */

Office.onReady((info) => {
  if (info.host === Office.HostType.Outlook) {
    document.getElementById("sideload-msg").style.display = "none";
    document.getElementById("app-body").style.display = "flex";
    document.getElementById("run").onclick = run;
  }
});


// Outlook instructions below
export async function run() {
// Get a reference to the current message
const item = Office.context.mailbox.item;

/* If extension enabled
    If send -> check email for image
      if an image is found pass the image to Controller 
        */
// Write message property value to the task pane
document.getElementById("item-subject").innerHTML = "<b>Subject:</b> <br/>" + item.subject;
}
