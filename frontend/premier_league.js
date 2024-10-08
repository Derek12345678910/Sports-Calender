import dayjs from 'https://unpkg.com/dayjs@1.11.10/esm/index.js'
import { fetchApi } from './data/apirequest.js'

const today = dayjs();
const formattedDate = today.format('YYYY-MM-DD')
console.log(formattedDate)

document.querySelector('.date-input').value = formattedDate

let gamesHTML = '';


let premierLeague;

console.log(typeof fetchApi('soccer','english'));

fetchApi('soccer','english')
    .then(data=>{
        premierLeague = data;
        console.log(premierLeague.league_name)
        
    })
    .catch(error =>{
        console.log('Error', error)
    }
    )



/*games.forEach(game =>{
    gamesHTML+= `
    <div class="game-container">
        <div class="team1-container">
            <
        </div>
    </div>    
    `
})
    */