function fileValidation() {
    let fileInput = document.getElementById('post_file');

    console.log(fileInput.value);

    let filePath = fileInput.value;
    let allowedExtensions = ['.jpg', '.jpeg', '.png'];
    x = 0
    for (extension in allowedExtensions) {

        if (filePath.includes(allowedExtensions[extension])) {
            x++;
            console.log(`${filePath} contains ${allowedExtensions[extension]}, so x is now at ${x}`)
            console.log(`the value of index ${extension} is ${allowedExtensions[extension]}`)
        }
        else {};
        console.log(`${filePath} does not contain ${allowedExtensions[extension]}, so x is now at ${x}`)
    }
    if (x < 1) {
        alert(
            'Your file does not have the correct format. Allowed formats: jpg, jpeg, png.'
        );
        fileInput.value = '';
    }
    
};

console.log("Javascript is working");


