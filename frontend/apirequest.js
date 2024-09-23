let url = 'http://127.0.0.1:5000/'

// communicates with app.py to grab json file
function fetchApi(sport){
    const params = new URLSearchParams();
    params.append('sport', sport);

    const fullUrl = `${url}?${params.toString()}`;

    fetch(fullUrl)
    .then(response => {
        // Check if response is OK
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // return json file of sport information
        return response.json()
    })
}