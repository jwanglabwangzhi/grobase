Vue.component('template-b',{
  template: '#template-a',
  props: {
    dataNum: {
      type: Number,
      default: 100
    },
    cur: {
      type: Number,
      default:1
    },
    each: {
      type: Number,
      default: 10
    },
    visiblepage: {
      type: Number,
      default: 10
    }
  },
  data: function(){
    return {
      curPage:0
    }
  },
  created: function(){
    this.curPage = this.cur;
  },
  computed: {
    totalPages: function(){
      return Math.ceil(this.dataNum / this.each) || 0
    },
    pages: function(){
      var lowPage = 1;
      var highPage = this.totalPages;
      var pageArr = [];
      if(this.totalPages > this.visiblepage){
        var sub = Math.ceil(this.visiblepage/2);
        if(this.curPage > sub && this.curPage < this.totalPages - sub +1){
          lowPage = this.curPage - sub;
          highPage = this.curPage + sub - 2;
        }else if(this.curPage <= sub){
          lowPage = 1;
          highPage = this.visiblepage;
        }else{
          lowPage = this.totalPages - this.visiblepage + 1;
          highPage = this.totalPages;
        }
      }
      while(lowPage <= highPage){
        pageArr.push(lowPage);
        lowPage ++;
      }
      return pageArr;
    }
  },
  methods: {
    btnClick: function(index){
      this.curPage = index;
      this.$emit('change-page', index)
    }
    , nextClick: function() {
      if (this.curPage < this.totalPages) {
        this.curPage++;
        this.$emit('change-page', this.curPage)
      }
    }
    , prevClick: function() {
      if (this.curPage > 1) {
        this.curPage--;
        this.$emit('change-page', this.curPage)
      }
    }
  }    
})


new Vue({
  el:'#app',
  data:{
   gridColumns: ['name', 'power'],
   pagedata: [
   { name: 'Chuck Norris', power: Infinity },
   { name: 'Bruce Lee', power: 9000 },
   { name: 'Jackie Chan', power: 7000 },
   { name: 'Jackie Chan', power: 7000 },
   { name: 'Jackie Chan', power: 7000 }, 
   { name: 'Jackie Chan', power: 7000 },     
   { name: 'Chuck Norris', power: Infinity },  
   { name: 'Jet Li', power: 8000 },
   { name: 'Jackie Chan', power: 7000 },
   { name: 'Jackie Chan', power: 7000 },
   { name: 'Jackie Chan', power: 7000 }, 
   { name: 'Jackie Chan', power: 7000 },     
   { name: 'Chuck Norris', power: Infinity },  
   { name: 'Jet Li', power: 8000 }       
   ],
    cur: 0, 
    dataNum: 0, 
    eachPageSize: 3, 
    visiblepage: 5, 
    //pagedata: [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11], 
    curpage: 1    
  },
  computed: {
    curList: function () {
      var p = [];
      for(var i = 0,l= this.pagedata.length;i<l;i++){
        p[i] = this.pagedata[i];
      }
      return p.splice((this.curpage-1) * this.eachPageSize, this.eachPageSize);
    }
  }, 
  methods: {
    changePage: function (cur) {
      this.curpage = cur;
    }
  }
}) 