<template>
  <div>
    <p>{{ ticket.title }}</p>
    <p>{{ ticket.notes }}</p>
    <p>{{ ticket.completed }}</p>
    <p>{{ ticket.assigned_to }}</p>
  </div>
</template>

<script>
export default {
  props: ['ticket'],
}
</script>