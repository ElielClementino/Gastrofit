<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      width="1024"
    >
      <v-card
      style="box-shadow: -2px 1px 18px 12px rgba(103,232,249,1);"
      >
        <v-card-title class="form-header">
          <span class="text-h3">{{ editing ? "Editando o ingrediente" : "Cadastro de Ingredientes" }}</span>
        </v-card-title>
        <v-card-text>
        <small>*Preecha todos os campos de acordo com as informações do ingrediente.</small>
          <v-container>
            <v-row>
            <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Nome"
                  class="custom-input-box"
                  v-model="ingredient.name"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Marca"
                  class="custom-input-box"
                  v-model="ingredient.brand"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Quantidade(gramas)"
                  class="custom-input-box"
                  v-model.number="ingredient.amount"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Carboidratos"
                  class="custom-input-box"
                  v-model.number="ingredient.carbohydrate"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Proteína"
                  class="custom-input-box"
                  v-model.number="ingredient.protein"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Gordura Trans"
                  class="custom-input-box"
                  v-model.number="ingredient.trans_fat"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Gordura Saturada"
                  class="custom-input-box"
                  v-model.number="ingredient.saturated_fat"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Gordura Total"
                  class="custom-input-box"
                  v-model.number="ingredient.total_fat"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Fibra"
                  class="custom-input-box"
                  v-model.number="ingredient.fiber"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="8"
                md="6"
              >
                <v-text-field
                  label="Sódio"
                  class="custom-input-box"
                  v-model.number="ingredient.sodium"
                  required
                  outlined
                  dense
                  hide-details
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue-darken-1"
            variant="text"
            @click="closeDialog"
          >
            Fechar
          </v-btn>
          <v-btn
            color="blue-darken-1"
            variant="text"
            @click="saveIngredient"
          >
            {{ creating ? "Cadastrar" : "Salvar"}}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import ingredientsApi from "@/api/ingredients.js"

  export default {
    data: () => ({
      dialog: false,
      editing: false,
      creating: false,
      ingredient: {
        name: null,
        brand: null,
        amount: 0,
        carbohydrate: 0,
        protein: 0,
        trans_fat: 0,
        saturated_fat: 0,
        total_fat: 0,
        fiber: 0,
        sodium: 0,
      }
    }),
    props: {
      addingIngredient: {
        type: Boolean,
        default: false,
      },
      ingredientToEdit: {
        type: Object,
        required: false,
      },
    },
    watch: {
      ingredientToEdit (val) {
        this.editing = true
        this.ingredient = val
        this.showPopup()
      },
      addingIngredient (val) {
        this.creating = true
        this.showPopup()
      }
    },
    methods: {
      resetForm () {
        let ingredient = {
          "name": null,
          "brand": null,
          "amount": 0,
          "carbohydrate": 0,
          "protein": 0,
          "trans_fat": 0,
          "saturated_fat": 0,
          "total_fat": 0,
          "fiber": 0,
          "sodium": 0,
        }
        this.editing = false
        this.creating = false
        this.ingredient = ingredient
      },
      saveIngredient () {
        if (this.creating) {
          ingredientsApi.addIngredient(this.ingredient)
        }
        if (this.editing) {
          ingredientsApi.editIngredient(this.ingredient?.id, this.ingredient)
        }
        this.closeDialog()
      },
      showPopup () {
        this.dialog = true
      },
      closeDialog () {
        this.resetForm()
        this.dialog = false
      }
    }
  }
</script>

<style scoped>
  .form-header span::after {
      content: '';
      display: block;
      width: 98%;
      height: 0.3rem;
      background-color: #67e8f9;
      margin: 5px auto;
      position: absolute;
      border-radius: 10px;
  }

  .custom-input-box:focus-within {
    outline: 1px solid #67e8f9;
    border-radius:5px
  }

</style>