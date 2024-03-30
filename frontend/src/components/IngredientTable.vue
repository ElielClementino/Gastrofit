<template>
  <v-card>
    <IngredientForm
      :addingIngredient="addingIngredient"
      :ingredientToEdit="ingredientToEdit"
    />
    <v-btn
      color="blue-darken-1"
      block
      class="mt-8"
      @click="addIngredient"
    >
      Cadastrar ingredientes
    </v-btn>
    <v-text-field
      class="mb-4"
      v-model="search"
      prepend-inner-icon="mdi-magnify"
      label="Buscar"
      single-line
      hide-details
    ></v-text-field>
    <v-divider></v-divider>
  <v-data-table
    :items-per-page="itemsPerPage"
    :headers="headers"
    :items="ingredients"
    :loading="loading"
    :search="search"
    loading-text="Carregando os ingredients, por favor, espere."
    :sort-by="[{ key: 'calory', order: 'asc' }]"
  >
    <template v-slot:top>
        <v-dialog v-model="dialogDelete" max-width="600px">
          <v-card>
            <v-card-title class="text-h5">Tem certeza que deseja deletar esse ingrediente ?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancelar</v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">Confirmar</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
    </template>
    <template v-slot:item.actions="{ item }">
        <v-sheet class="d-flex">
          <div>
              <v-icon
                  size="large"
                  @click="editItem(item)"
              >
                  mdi-pencil
              </v-icon>
              <v-tooltip
                      activator="parent"
                      location="top"
                  >
                      Editar ingrediente
              </v-tooltip>
          </div>
          <div>   
              <v-icon
                  size="large"
                  @click="deleteItem(item)"
              >
                  mdi-delete
              </v-icon>
                  <v-tooltip
                      activator="parent"
                      location="top"
                  >
                      Deletar ingrediente
                  </v-tooltip>
          </div>
        </v-sheet>
    </template>
    <template v-slot:bottom>
      <div class="text-center pt-2">
        <v-pagination
          v-model="page"
          :length="totalPages"
          @update:page="listIngredients(page)"
        ></v-pagination>
      </div>
    </template>
  </v-data-table>
  </v-card>
</template>


<script>
import ingredientsApi from "@/api/ingredients.js"
import IngredientForm from "@/components/IngredientForm.vue"

  export default {
    components: {
      IngredientForm,
    },
    data: () => ({
      dialog: false,
      loading: false,
      search: '',
      page: 1,
      itemsPerPage: 15,
      totalPages: 0,
      dialogDelete: false,
      headers: [
        {
          title: 'Ingredientes (Aproximados à 100g )',
          align: 'start',
          sortable: false,
          value: 'name',
          key: 'name',
        },
        { title: 'Calorias', key: 'calory' },
        { title: 'Carboidratos(g)', key: 'carbohydrate' },
        { title: 'Proteinas(g)', key: 'protein' },
        { title: 'Gord Trans(g)', key: 'trans_fat' },
        { title: 'Gord Sat(g)', key: 'saturated_fat' },
        { title: 'Gord Total(g)', key: 'total_fat' },
        { title: 'Fibras(g)', key: 'fiber' },
        { title: 'Sódio', key: 'sodium' },
        { title: 'Actions', key: 'actions', sortable: false },
      ],
      ingredients: [],
      editedIndex: -1,
      ingredientToEdit: {},
      addingIngredient: false,
      defaultItem: {
        name: '',
        calory: 0,
        total_fat: 0,
        carbohydrate: 0,
        protein: 0,
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
      page () {
        this.listIngredients()
      }
    },

    mounted () {
      this.listIngredients()
    },

    methods: {
      async listIngredients() {
        this.loading = true
        try {
          const data = await ingredientsApi.listIngredients(this.page) 
          this.ingredients = data.ingredients
          this.totalPages = data.total_pages
        } catch (error) {
            console.log("Erro ao carregar os ingredientes: ", error)
        } finally {
          this.loading = false
        }
      },
      addIngredient () {
        this.addingIngredient = true
      },
      editItem (item) {
        this.ingredientToEdit = item
        this.addingIngredient = false
      },

      deleteItem (item) {
        this.editedIndex = this.ingredients.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.ingredients.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.ingredients[this.editedIndex], this.editedItem)
        } else {
          this.ingredients.push(this.editedItem)
        }
        this.close()
      },
    },
  }
</script>