var vm = new Vue({
    el: '#app9',
    data: {
        l1_array: [],
        select1:'human',
        select2:'cell_1',   
        select3:'nac1',            
        l2_list:[],
        l2_sort_list:[],
        l3_list:[],
        l3_sort_list:[],
        l2_array:[],
        l3_array:[],
        l3_super_array:[]
    },
    created:function(){
        var self=this;
        reqwest({
            url:'http://127.0.0.1:8000/relate_select_json/species_json/?format=json',
            type:'json',
            method:'get',
            success:function(response_data){
                self.l1_array = response_data;
                self.l1_array[0].is_active=true; 
                self.get_l2_array();
                self.get_l3_array(); 
                self.l2_l3_init_activate();
                
            }
        }); 
           
    },
    methods:{ 
        make_l1_inactive: function(){
            for(var i=0; i<this.l1_array.length;i++){
                this.l1_array[i].is_active = false;
            }
        },
        make_l2_inactive: function(){
            for(var i=0; i<this.l2_array.length;i++){
                this.l2_array[i].is_active = false;
            }
        }, 
        make_l3_inactive: function(){
            for(var i=0; i<this.l3_array.length;i++){
                this.l3_array[i].is_active = false;
            }
        },         
        item_active: function(item){    
            item.is_active = !item.is_active;           
        },           
        change_select1:function(item){
            this.select1=item.specie_name;
        },
        change_select2:function(item){
            this.select2=item.source_name;
        },   
        change_select3:function(item){
            this.select3=item.process_name;
        },         
        get_l2_array: function(){
            var new_l2 = new Array();
            for(var i in this.l1_array){
                var obj= this.l1_array[i];
                if (obj.specie_name==this.select1){
                    this.l2_array=obj.sources;
                    break;
                }
            }              
            for(var j in this.l2_array){
                var obj1=this.l2_array[j];
                new_l2.push(obj1.source_name);
            }
            this.l2_sort_list=new_l2.sort(); 
        },
        get_l3_array: function(){       
            var new_l3 = new Array();
            var new_array_l3 = new Array()
            for(var i in this.l2_array){
                var obj=this.l2_array[i];
                if (obj.source_name == this.select2){
                    this.l3_array=obj.process;
                    break;
                }    
            }
            for(var j in this.l3_array){
                var obj1=this.l3_array[j];
                new_l3.push(obj1.process_name);
                new_array_l3.push({id:this.select1,source:this.select2,process_name:obj1.process_name})
            }
            this.l3_sort_list=new_l3.sort();   
            this.l3_super_array=new_array_l3;
        },
        //get_table_data:function(){
        //vm_table.tableData=this.l3_super_array;}
        l2_l3_init_activate:function(){
            this.l2_array[0].is_active=true;
            this.l3_array[0].is_active=true;     
        }        
    },   
    computed:{
        l2_update: function () {
            this.get_l2_array();
            this.get_l3_array();
        },
        l3_update: function () {
            this.get_l3_array();
        }
    }
}); 


