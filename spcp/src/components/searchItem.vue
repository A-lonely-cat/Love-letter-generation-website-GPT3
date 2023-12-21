<template>
    <div class="item">
        <slot></slot>
    </div>
</template>

<script setup>

</script>

<style scoped>
.item {
    display: flex;
    justify-content: center;
    align-items: center;
    transition: transform 0.2s;
    /* 设置变换过渡时间 */
    border-radius: 20px;
    width: 60px;
    /* 设置盒子的宽度 */
    height: 50px;
    /* 设置盒子的高度 */
    background-color: white;
    /* 设置盒子的背景颜色 */
    margin: 10px;
    border: 1px solid black;
    padding: 20px 20px 20px 20px;
    font-size: 30px;
}

.item:hover {
    transform: scale(1.1);
    /* 设置放大倍数，此处为1.2倍 */
}
</style>