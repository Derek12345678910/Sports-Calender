import dayjs from 'https://unpkg.com/dayjs@1.11.10/esm/index.js'
import { fetchApi } from './data/apirequest.js'


const today = dayjs();
const formattedDate = today.format('YYYY-MM-DD')
console.log(formattedDate)

document.querySelector('.date-input').value = formattedDate
