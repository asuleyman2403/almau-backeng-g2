const BASE_URL = 'http://localhost:8000';

const fetchBlogs = () => {
    const xhr = new XMLHttpRequest();

    xhr.open('GET', `${BASE_URL}/blogs`);


    xhr.onload = function() {
        console.log(xhr.response);
    }

    xhr.send();
}

fetchBlogs();