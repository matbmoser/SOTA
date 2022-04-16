<?php

class Usuario
{
    private $dbHost     = "localhost";
    private $dbUsername = "id11631880_matbmoser";
    private $dbPassword = "a(dux>kqT%IMr(=7";
    private $dbName     = "id11631880_hypetech";
    private $table      = "producto";


    public function __construct(){
        
        if(!isset($this->db)){
            // Connect to the database
            $conn = new mysqli($this->dbHost, $this->dbUsername, $this->dbPassword, $this->dbName);
            if($conn->connect_error){
                die("Failed to connect with MySQL: ".$this->table. $conn->connect_error);
            }else{
                $this->db = $conn;
            }
        }
    }

    /*
     * Returns rows from the database based on the conditions
     * @param array select, where, order_by, limit and return_type conditions
     */
    public function getRows($conditions = array()){
        $sql = 'SELECT ';
        $sql .= array_key_exists("select",$conditions)?$conditions['select']:'*';
        $sql .= ' FROM '.$this->table;
        if(array_key_exists("where",$conditions)){
            $sql .= ' WHERE ';
            $i = 0;
            foreach($conditions['where'] as $key => $value){
                $pre = ($i > 0)?' AND ':'';
                $sql .= $pre.$key." = '".$value."'";
                $i++;
            }
        }