const form = document.getElementById('mainForm')
const postButton = document.getElementById('toDb')

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
