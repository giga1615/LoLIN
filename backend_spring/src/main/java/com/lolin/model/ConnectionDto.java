package com.lolin.model;

public class ConnectionDto {
	String id;
	String connectionCheck;

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getConnectionCheck() {
		return connectionCheck;
	}

	public void setConnectionCheck(String connectionCheck) {
		this.connectionCheck = connectionCheck;
	}

	@Override
	public String toString() {
		return "ConnectionDto [id=" + id + ", connectionCheck=" + connectionCheck + "]";
	}

}
