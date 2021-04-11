package com.lolin.model;

public class MyRoomListDto {

	String roomNumber;
	String roomName;

	public MyRoomListDto(String roomNumber, String roomName) {
		super();
		this.roomNumber = roomNumber;
		this.roomName = roomName;
	}

	public String getRoomNumber() {
		return roomNumber;
	}

	public void setRoomNumber(String roomNumber) {
		this.roomNumber = roomNumber;
	}

	public String getRoomName() {
		return roomName;
	}

	public void setRoomName(String roomName) {
		this.roomName = roomName;
	}

	@Override
	public String toString() {
		return "MyRoomListDto [roomNumber=" + roomNumber + ", roomName=" + roomName + "]";
	}

}
