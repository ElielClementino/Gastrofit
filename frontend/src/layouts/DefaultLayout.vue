<template>
  <VLayout>
    <VApp>
      <NavBar/>
      <VMain>
        <RouterView />
      </VMain>
      <Footer/>
    </VApp>
  </VLayout>
</template>

<script>
import NavBar from "../components/NavBar.vue"
import Footer from "../components/Footer.vue"

export default {
  name: "DefaultLayout",
  components: {
    NavBar,
    Footer,
  },
}
</script>