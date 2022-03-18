
function fileValidation() {
    let fileInput = document.getElementById('post_file');

    console.log(fileInput.value);

    let filePath = fileInput.value;
    let allowedExtentions = ['.jpg', '.jpeg', '.png'];

    let allowed = true

    // if (filePath.includes('.jpg')||(filePath.includes('.jpeg')||(filePath.includes('.png')){
    //     console.log('allowed!')
    // }
    // else{
    //     console.log('not allowed')
    // }
    for (extension in allowedExtentions) {
        
        if (filePath.includes(extension)) { 
            allowed = true;
            break;
        }
        else {
            allowed = false
        };
        console.log(filePath)
        console.log(allowed)
    }
    if (allowed == false) {
        alert(
            'Your file does not have the correct format. Allowed formats: jpg, jpeg, png.'
        );
        fileInput.value = '';
    }
};

console.log("Javascript is working");
