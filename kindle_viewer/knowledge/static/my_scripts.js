

function screens(){
    let image = document.getElementById('photos');
    let images = ['static/image1.JPG','static/image2.JPG','static/image3.JPG','static/kindle.jpg']
    setInterval(function(){
        let random = Math.floor(Math.random() * 4);
        image.src = images[random];
    }, 800);
}