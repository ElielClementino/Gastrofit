import api from "./config.js"

export default {
    listIngredients: (page) => {
        return new Promise((resolve, reject) => {
            api.get("api/culinary/list/ingredients/", { params: { page } })
            .then((response) => {
                return resolve(response.data)
            }).catch((error) => {
                return reject(error)
            })
        })
    },

    addIngredient: (ingredient) => {
        return new Promise((resolve, reject) => {
            api.post("api/culinary/new/ingredient/", ingredient)
            .then((response) => {
                return resolve(response)
            }).catch((error) => {
                return reject(error)
            })
        })
    },

    editIngredient: (ingredientId, editedIngredient) => {
        return new Promise((resolve, reject) => {
            api.patch(`api/culinary/update/ingredient/${ingredientId}/`, editedIngredient)
            .then((response) => {
                return resolve(response)
            }).catch((error) => {
                return reject(error)
            })
        })
    },

    deleteIngredient: (ingredientId) => {
        return new Promise((resolve, reject) => {
            api.post(`api/culinary/delete/ingredient/${ingredientId}/`)
            .then((response) =>{
                return resolve(response)
            }).catch((error) => {
                return reject(response)
            })
        })
    }
}