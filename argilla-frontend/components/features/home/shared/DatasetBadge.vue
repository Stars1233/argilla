<template>
  <div class="dataset-badge">
    <span v-if="icon" class="dataset-badge__icon-wrapper"
      ><svgicon :name="icon" :color="color" class="dataset-badge__icon"
    /></span>
    <span class="dataset-badge__text">{{ text }}</span>
  </div>
</template>

<script>
import "assets/icons/text-classification";
import "assets/icons/question-answering";
import "assets/icons/text-to-image";
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
    icon: {
      type: String,
    },
    color: {
      type: String,
    },
    fontSize: {
      type: String,
      default: "12px",
    },
  },
};
</script>
<style lang="scss" scoped>
.dataset-badge {
  display: flex;
  align-items: center;
  height: calc(v-bind(fontSize) * 2);
  border: 1px solid var(--bg-opacity-10);
  border-radius: $border-radius-xl;
  font-size: v-bind(fontSize);
  background: linear-gradient(
    90deg,
    hsl(from v-bind(color) h s l / 10%) 0%,
    hsl(from v-bind(color) h s l / 1%) 30px
  );

  &__icon-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: calc($base-space / 1.8) $base-space;
    border-radius: $border-radius-xl;
    & + .dataset-badge__text {
      padding: calc($base-space / 2) $base-space calc($base-space / 2)
        calc($base-space / 2);
    }
  }
  &__icon {
    fill: v-bind(color);
    width: 16px;
    height: 16px;
  }
  &__text {
    font-weight: 400;
    color: var(--fg-secondary);
    padding: calc($base-space / 2) $base-space;
  }
}
</style>
