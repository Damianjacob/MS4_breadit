function fileValidation() {
    /*
    Checks if the file the user wants to upload is 
    one of the allowed file extensions, if it 
    isn't, sets the value of the file input
    back to an empty string and alerts the user.
    */
    let fileInput = document.getElementById('post_file');
    let messageDiv = document.getElementById('custom-message-div');
    let messageP = document.getElementById('custom-message-p');

    console.log(fileInput.value);

    let filePath = fileInput.value;
    let allowedExtensions = ['.jpg', '.jpeg', '.png'];
    x = 0;
    for (let extension in allowedExtensions) {

        if (filePath.includes(allowedExtensions[extension])) {
            x++;
        }
        else { }
    }
    if (x < 1) {
        messageDiv.style.display = 'block';
        messageP.textContent =
            'This file type is not allowed. Allowed formats: jpg, jpeg, png.';
        fileInput.value = '';
    }
}

// Makes the custom message div disappear by clicking on it
let message = document.getElementById('custom-message-div');
message.addEventListener("click", function () {
    message.style.display = 'none';
});
