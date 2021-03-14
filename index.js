const { makeExecutableSchema } = require('graphql-tools')
const express = require('express')
const { graphqlHTTP } = require('express-graphql')
const { readFileSync } = require('fs')
const { join } = require('path')
const resolvers = require('./lib/resolvers')
const { ApolloServer } = require('apollo-server');

const app = express()
const port = process.env.port || 3000

// Definiendo el squema
const typeDefs = readFileSync(
    join(__dirname, 'lib', 'schema.graphql'),
    'utf-8'
)
//const schema = makeExecutableSchema({ typeDefs, resolvers })
const server = new ApolloServer({ typeDefs, resolvers })


app.use('/api', graphqlHTTP({
    schema: server,
    rootValue: resolvers,
    graphiql: true
}))

server.listen(port, () => {
    console.log(`Server is listening at http://localhost:${port}/api`)
})