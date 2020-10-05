<template>
  <div>
    <video
      autoplay="autoplay"
      muted="muted"
      loop="loop"
      id="mobile_video"
      playsinline=""
    >
      <source src="@/assets/main.mp4" type="video/mp4" />
    </video>

    <div
      style="position: absolute; top: 35%; left: 38%; margin: -50px 0 0 -50px"
    >
      <p style="color: white; font-size: 450%">주식의 첫 걸음</p>
      <br />
      <v-img
        src="@/assets/green.png"
        style="border-radius: 50px; cursor: pointer"
        @click="$router.push('/home')"
      />
      <br />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style>
#mobile_video {
  z-index: -1;
  position: fixed;
  top: 0;
  left: 0;
  min-width: 100%;
  min-height: 100vh;
  width: 100%;
  height: auto;
  opacity: 0.7;
}
</style>