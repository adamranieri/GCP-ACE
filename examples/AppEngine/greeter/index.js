import express from 'express'
const app = express()

app.get('/hello', (req, res) => {
    res.send(`Sup random person V3`)
})

app.get('/hello/:name', (req, res) => {
    const name = req.params.name
    res.send(`Hello ${name} V3`)
})

const PORT = process.env.PORT || 3000
app.listen(PORT, ()=>console.log(`Listening on port ${PORT}`))


