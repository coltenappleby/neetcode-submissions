class LinkedNode {
    constructor(val, next_node = null){
        this.val = val
        this.next = next_node
    }
}


class LinkedList {
    constructor() {
        this.head = new LinkedNode(-1);
        this.tail = this.head;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let node = this.head.next
        let i = 0
        while(node){
            if(i === index){
                return node.val
            }
            i++
            node = node.next
            
        }
        return -1
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        let newNode = new LinkedNode(val)
        newNode.next = this.head.next
        this.head.next = newNode
        if(this.tail === this.head){
            this.tail = newNode
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        let newNode = new LinkedNode(val)
        this.tail.next = newNode
        this.tail = newNode
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let i = 0;
        let curr = this.head;
        while (i < index && curr) {
            i++;
            curr = curr.next;
        }

        // Remove the node ahead of curr
        if (curr && curr.next) {
            if (curr.next === this.tail) {
                this.tail = curr;
            }
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let values = []
        let node = this.head.next;
        while(node){
            values.push(node.val)
            node = node.next
        }
        return values
    }
}
