<template>
  <footer class="bg-cyan-300 p-10">
    <div class="flex justify-center items-center space-x-4">
      <a v-for="(link, index) in links" :href="link" target="_blank" class="text-white cursor-pointer text-4xl">
        <i :class="icons[index] + ' px-4 h-8 w-6'"></i>
      </a>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      links: [
        "https://github.com/ElielClementino",
        "https://www.linkedin.com/in/eliel-clementino-3070b0224/"
      ],
      icons: [
        "bi bi-github",
        "bi bi-linkedin"
      ]
    };
  },
};
</script>

