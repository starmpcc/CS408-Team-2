import React, {useState} from 'react';
import '../App.css';
import {Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';

export default function Select() {
    let [소설명1, 소설명1변경] = useState('소설명1');
    let [소설명2, 소설명2변경] = useState('소설명2');
    let [소설명3, 소설명3변경] = useState('소설명3');
    let [소설명4, 소설명4변경] = useState('소설명4');
    return(
        <>
            <div className='title'> 작성 중인 소설 선택 화면</div>
            <Link to = '/write'>
                <Button>{소설명1}</Button>
            </Link>
            <Link to = '/write'>
                <Button>{소설명2}</Button>
            </Link>
            <Link to = '/write'>
                <Button>{소설명3}</Button>
            </Link>
            <Link to = '/write'>
                <Button>{소설명4}</Button>
            </Link>
            
            
            
            
        </>
    )
}