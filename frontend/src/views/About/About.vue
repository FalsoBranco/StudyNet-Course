<script>
import Hero from '../../layout/Hero.vue'
import Section from '../../layout/Section.vue'
import Container from '../../layout/Container.vue'
export default {
  name: 'About',
  setup() {
    return {}
  },
  components: { Hero, Section, Container },
}
</script>

<template>
  <div class="home">
    <Hero>
      <span> Welcome to StudyNet </span>
    </Hero>
    <Section>
      <Container>
        <p>This is the about page</p>
      </Container>
    </Section>
  </div>
</template>
