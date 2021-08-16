<template>
  <div class="register">
    <div class="container-fluid">
        <div class="row px-5">
            <div class="col-5 px-4 pt-4 display-content">
                <h3 class="logo text-left">Budget Me</h3>
            </div>
            <div class="col-7 px-4 pt-4 register-content">
                <p class="text-right">Already have an account? <router-link to="/" style="color:var(--primary-color)">Sign in</router-link></p>
                <div class="register-component text-center px-4">
                    <strong>Sign up to Budget Me</strong>
                    <div class="signup-with mt-4 mb-5">
                        <button type="button" class="btn btn-light btn-sign-with-account"><i class="bi bi-google"></i> Sign Up with Google</button>
                    </div>
                    <h6 class="line pt-4"><span>or sign up with email</span></h6>
                    <form class="sign-with-email-form">
                        <div class="form-group">
                            <label for="exampleInputEmail1">Email address</label>
                            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                        </div>
                        <button type="button" class="btn btn-block btn-primary">Create Account</button>
                    </form>
                </div>
            </div>
        </div>    
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Register',
  components: {},
});
</script>
<style scoped>
.register{
    background-color: var(--background-color-secondary);
    height: 100vh;
    color: var(--primary-color);
    padding: 2.5rem 0;
}
.logo{
    color: var(--primary-color);
    font-weight: 600;
}
.display-content{
    background-color: var(--background-color-secondary-2);
    height: calc(100vh - 5rem);
    border-radius: 10px 0 0 10px;
}
.register-content{
    background-color: var(--background-color-primary);
    height: calc(100vh - 5rem);
    border-radius: 0 10px 10px 0;
}
.register-component{
    width: 95%;
    margin: 6.5rem auto 0 auto;
}
.sign-with-email-form{
    margin-top: 4.5rem;
}
</style>
