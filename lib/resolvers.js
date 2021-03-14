const users = require('./db.js')

module.exports = {
    Query: {
        getUsers: () => {
            return users
        },
        getUser: (root, args) => {
            const user = users.filter(user => user._id === args.id)
            return user.pop();
        }
    }
}