import React, {useState} from 'react';
import '../App.css';
import {Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';

export default function Warning() {
    return(
        <>
        <div className = 'title'>경고</div>
        <p>정말 나가시겠습니까? 저장하지 않고 나갈 경우 모든 진행 상황을 잃게 됩니다.</p>
        <Link to = '/'>
            <Button>저장하고 나가기</Button>
        </Link>
        <Link to = '/'>
            <Button>저장하지 않고 나가기</Button> 
        </Link>
        
        </>
    )
}