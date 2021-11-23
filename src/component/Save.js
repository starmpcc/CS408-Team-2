import React, {useState} from 'react';
import '../App.css';
import {Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';

export default function Save(){
    return(
        <>
            <div className="title">저장</div>
            <p>저장하시겠습니까?</p>
            <Link to = '/write'>
                <Button>예</Button>
            </Link>
            
            <Link to = '/write'>
                <Button>아니오</Button>
            </Link>
            
        </>
    )
}