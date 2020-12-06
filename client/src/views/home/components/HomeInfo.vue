<template>
    <div class="home-info-body">
        <div class="rotating-text">
            <p>OctoberRain is a Blog for</p>
            <p class="switch-word">
                <span class="word alizarin">creating.</span>
                <span class="word wisteria">learning.</span>
                <span class="word peter-river">sharing.</span>
                <span class="word emerald">recording.</span>
                <span class="word sun-flower">amusing.</span>
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: "",
    data() {
        return {
            words: [],
            currentWordIndex: null,
            maxWordIndex: null,
            currentWord: null,
            timer: null
        }
    },
    methods: {
        changeWordsStyle() {
            this.words = document.querySelectorAll(".word")
            this.words.forEach((word) => {
                let letters = word.textContent.split("")
                // console.log(word.textContent);
                word.textContent = ""
                letters.forEach((letter) => {
                    let span = document.createElement("span")
                    span.textContent = letter
                    // console.log(word.textContent);
                    span.className = "letter"
                    // console.log(span);
                    word.append(span)
                    // console.log(word);
                })
            })
            this.currentWordIndex = 0
            this.maxWordIndex = this.words.length - 1
            this.words[this.currentWordIndex].style.opacity = "1"
        },
        rotateText() {
            this.currentWord = this.words[this.currentWordIndex]
            let nextWord =
                this.currentWordIndex === this.maxWordIndex
                    ? this.words[0]
                    : this.words[this.currentWordIndex + 1]
            // console.log(nextWord)
            // rotate out letters of current word
            Array.from(this.currentWord.children).forEach((letter, i) => {
                setTimeout(() => {
                    letter.className = "letter out"
                    console.log(letter.className);
                }, i * 80)
            })
            // reveal and rotate in letters of next word
            nextWord.style.opacity = "1"
            // console.log(nextWord.children);
            Array.from(nextWord.children).forEach((letter, i) => {
                letter.className = "letter behind"
                setTimeout(() => {
                    letter.className = "letter in"
                    console.log(letter.className);
                }, 340 + i * 80)
                // console.log(letter.className);
            })
            this.currentWordIndex =
                this.currentWordIndex === this.maxWordIndex ? 0 : this.currentWordIndex + 1
        }
    },
    mounted() {
        this.changeWordsStyle()
        this.rotateText()
        this.timer = setInterval(this.rotateText, 4000)
    },
    beforeDestroy() {
        console.log('success');
        // clearTimeout(param);
        clearInterval(this.timer)
    },
}
</script>

<style lang="stylus">
.home-info-body
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh - 20rem;
    // background: #222;
    .rotating-text
        font-family: Lato, sans-serif;
        font-weight: 600;
        font-size: 5rem;
        color: white;
        transform: translateX(-12rem);
        p
            display: inline-flex;
            margin: 0;
            vertical-align: top;
        p + p 
            margin-left 1.4rem
            .word
                position: absolute;
                display: flex;
                opacity: 0;
                .letter
                    transform-origin: center center 25px;
                .out
                    transform: rotateX(90deg);
                    transition: 0.32s cubic-bezier(0.6, 0, 0.7, 0.2);
                .in
                    transition: 0.38s ease;
                .behind
                    transform: rotateX(-90deg);
.alizarin
    color: #e74c3c;
.wisteria
    color: #8e44ad;
.peter-river
    color: #3498db;
.emerald
    color: #2ecc71;
.sun-flower
    color: #f1c40f;
</style>
