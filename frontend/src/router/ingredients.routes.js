import DefaultLayout from "../layouts/DefaultLayout.vue"
import IngredientView from "../views/ingredients/IngredientView.vue"

export default [
    {
        path: "/ingredients/",
        component: DefaultLayout,
        children: [
            {
                path: "",
                name: "ingredients-list",
                component: IngredientView
            }
        ]
    }
]
