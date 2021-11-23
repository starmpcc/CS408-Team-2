import React, {useState} from 'react';
import '../App.css';
import {Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';


export default function Main() {
    return(
        <>
            <div className="title">
                한국어 대화형 소설 작성 시스템
            </div>
            <Link to = '/write'>
                <Button>
                새로운 소설 작성하기
                </Button>
            </Link>
            <Link to = '/select'>
                <Button>
                    불러오기
                </Button>
            </Link>
        </>
        
    )
}