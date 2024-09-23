import dayjs from 'https://unpkg.com/dayjs@1.11.10/esm/index.js'
import { fetchApi } from './data/apirequest.js'

let games = [];

const today = dayjs();
const formattedDate = today.format('YYYY-MM-DD')
console.log(formattedDate)

document.querySelector('.date-input').value = formattedDate

let gamesHTML = '';

games.forEach(game =>{
    gamesHTML+= `
    <div class="game-container">
        <div class="team1-container">
            <img class="team1-image" src="${game.image1}">
        </div>
    </div>    
    `
})