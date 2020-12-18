<template>
    <div class="body">
        <div class="chart" ref="chart"></div>
    </div>
</template>

<script>
export default {
    name: "ProfileBody",
    data() {
        return {
            chartInstance: null,
            data: null,
        }
    },
    mounted() {
        this.initChart()
        this.getData()
    },
    methods: {
        initChart() {
            this.chartInstance = this.$echarts.init(this.$refs.chart)
        },
        getData() {
            const data = [
                { name: "1", value: 99 },
                { name: "2", value: 69 },
                { name: "3", value: 79 },
                { name: "4", value: 29 },
                { name: "5", value: 89 },
                { name: "6", value: 49 },
                { name: "7", value: 39 },
            ]
            this.data = data
            this.updateChart()
        },
        updateChart() {
            const names = this.data.map(item => item.name)
            const values = this.data.map(item => item.value)
            console.log(names, values);
            const option = {
                xAxis: {
                    type: "value",
                },
                yAxis: {
                    type: "category",
                    data: names
                },
                series: [
                    {
                        type: "bar",
                        data: values
                    },
                ],
            }
            this.chartInstance.setOption(option)
        },
    },
}
</script>

<style lang="stylus" scoped>
.chart 
    max-width 50%
    height 30rem
</style>
