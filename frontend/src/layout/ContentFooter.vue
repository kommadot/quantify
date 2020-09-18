<template>
  <footer class="footer px-4">
    <div class="row align-items-center justify-content-lg-between">
      <div class="col-lg-6">
        <div class="copyright text-center text-lg-left text-muted">
          © {{year}}
          <a href="/" class="font-weight-bold ml-1" target="_blank">버핏보다싸핏</a>
        </div>
      </div>
      <div class="col-lg-6">
        <ul class="nav nav-footer justify-content-center justify-content-lg-end">
          <li class="nav-item px-1">김주형</li>
          <li class="nav-item px-1">김보성</li>
          <li class="nav-item px-1">박세종</li>
          <li class="nav-item px-1">심효빈</li>
        </ul>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      year: new Date().getFullYear(),
    };
  },
};
</script>
<style></style>
