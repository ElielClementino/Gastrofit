<template>
  <nav class="bg-cyan-300 text-gray-100 py-3 px-6 shadow md:flex justify-between items-center">
    <div class="flex items-center">
        <img src="../assets/logo.svg" class="h-8 w-auto">
        <h1 class="text-xl"> Gastrofit </h1>
    </div>

    <span @click="menuOpen()" class="absolute md:hidden right-6 top-1.5 cursor-pointer text-4xl">
        <i :class="[open ? 'bi bi-x' : 'bi bi-filter-left']"></i>
    </span>

    <ul class="md:flex md:items-center md:px-0 px-10 md:static absolute
    bg-cyan-300 md:w-auto w-full top-14 duration-300 ease-in"
    :class="[open ? 'left-0' : 'left-[-100%]']">
        <li class="md:mx-4 md:my-0 my-6" v-for="link in LINKS">
            <a :href="link.url" class="text-xl hover:text-gray-600 hover:border rounded-lg
            p-2 trasition duration-300 ease-in">
                {{link.name}}
            </a>
        </li>
    </ul>
  </nav>
</template>

<script>
    export default {
        setup() {
            const LINKS = [
                {name: "Página Inicial", url: "/"},
                {name: "Ingredientes", url: "ingredients"},
                {name: "Receitas", url: "#"},
                {name: "Dietas", url: "#"},
            ]
            return {LINKS}
        },
        data: () => ({
            open: false,
        }),
        methods: {
            menuOpen(open) {
                this.open = !this.open
            }
        }
    }
</script>
