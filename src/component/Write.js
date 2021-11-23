import React, {useState} from 'react';
import '../App.css';
import {Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';

export default function Write(){
    return(
        <>
            <div className='title'>소설 1</div>
            <Link to = '/Warning'>
                <Button>창 닫기</Button>
            </Link>
            
            <Link to = '/Save'>
                <Button>저장</Button>
            </Link>
            <Button>한 단계 전으로</Button>
            <Button>한 단계 후로</Button>
            <input></input>
            <Button>실행</Button>
        </>
    )
}