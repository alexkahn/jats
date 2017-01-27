<template>
    <a href="#">
        <li :class="{'removed': ticket.complete}" class="list-group-item">
            <div class="form-check">
                <label class="form-check-label" :for="ticketId">
                    <input :id="ticketId" class="form-check-input" type="checkbox" v-model="ticket.complete">
                    {{ ticket.title }}
                </label>
            </div>
        </li>
    </a>
</template>

<script>
    export default {
        props: ['ticket'],
        computed: {
            ticketId() {
                return "id_" + this.ticket.id;
            }
        }
    }
</script>