let url = 'http://127.0.0.1:5000/data'

// communicates with app.py to grab json file
export function fetchApi(sport, league){
    const params = new URLSearchParams();
    params.append('sport', sport);
    params.append('league', league);

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
    .then(data => {
        console.log(data);  // Log the received data
        return data
    })
    .catch(error => {
        console.error('Error:', error);
    });
}