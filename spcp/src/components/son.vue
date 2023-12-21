<template>
    <div class="container">
        <div class="box">盒子1</div>
        <div class="box">盒子2</div>
        <div class="box">盒子3</div>
        <div class="box">盒子4</div>
        <div class="box">盒子5</div>
        <div class="box">盒子6</div>
    </div>
</template>

<style scoped>
.box {
    transition: transform 0.2s;
    /* 设置变换过渡时间 */
    border-radius: 20px;
    width: 150px;
    /* 设置盒子的宽度 */
    height: 150px;
    /* 设置盒子的高度 */
    background-color: white;
    /* 设置盒子的背景颜色 */
    margin: 10px;
    border: 1px solid black;
    padding: 70px 70px 70px 70px;
    font-size: 30px;

}

.box:hover {
    transform: scale(1.1);
    /* 设置放大倍数，此处为1.2倍 */
}


.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    width: 80%;
    background-color: grba(1,1,1,0);
}

</style>

<script setup>

</script>