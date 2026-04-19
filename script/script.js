const form = document.getElementById('mainForm')
const postButton = document.getElementById('toDb')
const getBtn = document.getElementById('getALl')

form.addEventListener('submit', async (e) => {
    e.preventDefault()

    const data = {
        text: document.getElementById('textArea').value,
        tag: document.getElementById('tagInput').value
    }

    try {
        const responce = await fetch('http://127.0.0.1:8000/submit',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify(data)
        })

        const resultData = await responce.json()
        if (responce.ok) {
            console.log('Данные занесены в базу: ', resultData)
            form.reset();
        } else {
            console.log('Ошибка', resultData)
        }
        } catch(error) {
            console.error(error)
        }
})

async function loadData() {
    
    try {
        const responce = await fetch("http://127.0.0.1:8000/data")
        const data = await responce.json()

        const outputContainer = document.getElementById('output')
        outputContainer.innerHTML = ''

        data.forEach(item => {
            const div = document.createElement('div')
            div.textContent = `Текст: ${item.text}, Тэг: ${item.tag}`
            outputContainer.appendChild(div)
        
           
        });
    } catch (error) {
        console.error(error)
    }

    

    
}


