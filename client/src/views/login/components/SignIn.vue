<template>
  <div class="sign-in">
    <form class="form">
      <div class="input account">
        <input
          type="text"
          class="field"
          v-model="userInfo.username"
          autocomplete="on"
        />
        <label class="label">账号：</label>
      </div>
      <div class="input password">
        <input
          type="password"
          class="field"
          v-model="userInfo.password"
          autocomplete="on"
          @keyup.enter="handleClickLogin"
        />
        <label class="label">密码：</label>
      </div>
      <div class="button">
        <div type="submit" class="btn signin-btn" @click="handleClickLogin">
          登陆
        </div>
        <!-- <div class="btn signup-btn">注册</div> -->
      </div>
      <div class="switch">
        还没注册？点击<span class="register" @click="handleClickRegister"
          >注册</span
        >
      </div>
    </form>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "SignIn",
  props: {
    hasUser: Boolean,
  },
  data() {
    return {
      userInfo: {
        username: "",
        password: "",
        token: ""
      },
      hasThisUser: this.hasUser,
    };
  },
  methods: {
    handleClickLogin() {
      if (this.userInfo.username == "" || this.userInfo.password == "") {
        alert("输入内容不能为空！");
        return;
      }
      console.log(this.userInfo);
      this.$store.dispatch('signIn', this.userInfo)
      this.$router.push({path: '/'})
    },
    handleClickRegister() {
      this.hasThisUser = !this.hasThisUser;
      this.$emit("switch");
    },
  },
};
</script>

<style lang="stylus" scoped>
.sign-in {
  position: absolute;
  top: 50%;
  left: 50%;
  margin-top: -20rem;
  margin-left: -25rem;
  height: 40rem;
  width: 50rem;
  background-color: #958A8A40;
  border-radius: 1rem;

  .form {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 1rem;
    user-select: none;
    margin-top: 1rem;

    .input {
      position: relative;

      .field {
        width: 32rem;
        background-color: transparent;
        border: none;
        border-bottom: 0.1rem solid #0004;
        margin: 2rem 0;
        padding: 1rem 1.5rem 1.5rem 0;
        font-size: 1.6rem;
        color: #4b4b4b;
        text-indent: 6rem;

        &:focus {
          text-indent: 1rem;
        }

        &:focus~label {
          transform: translateY(-3.5rem);
          font-size: 1.4rem;
        }
      }

      .label {
        position: absolute;
        left: 0;
        font-size: 2rem;
        color: #4b4b4b;
        pointer-events: none;
        text-transform: uppercase;
        transition: all 0.3s;
        bottom: 3.4rem;
      }
    }

    .button {
      margin-top: 10.9rem;
      width: 25%;
      height: 3rem;
      border: 0.1rem solid #000;
      border-radius: 0.8rem;
      line-height: 3rem;
      font-size: 1.6rem;

      .signin-btn {
        color: #000;
        cursor: pointer;
        letter-spacing: 1rem;
        padding-left: 0.5rem;
      }
    }

    .switch {
      font-size: 1.6rem;
      margin-top: 3rem;
      letter-spacing: 0.12rem;

      .register {
        color: red;
      }
    }
  }
}
</style>
