// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0;

contract upload{
    string str;

    function write(string memory _str) public{
        str = _str;
    }

    function read () public view returns (string memory){
        return str;
    }
}