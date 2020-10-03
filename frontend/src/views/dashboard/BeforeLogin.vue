<template>
  <div>
    <video
      autoplay="autoplay"
      muted="muted"
      loop="loop"
      id="mobile_video"
      playsinline=""
    >
      <source
        src="https://s3.ap-northeast-2.amazonaws.com/alphasquare-s3/media/AP_1920_1080.mp4"
        type="video/mp4"
      />
    </video>

    <v-btn
      color="#00BCD4"
      style="position: absolute; left: 45%; top: 45%"
      @click="$router.push('/home')"
    >
      시작하기
    </v-btn>
  </div>
</template>

<script>
export default {};
</script>

<style>
#mobile_video {
  z-index: -1;
  position: fixed;
  top: 0;
  left: 0;
  min-width: 100%;
  min-height: 100vh;
  width: auto;
  height: auto;
  opacity: 70%;
}
</style>