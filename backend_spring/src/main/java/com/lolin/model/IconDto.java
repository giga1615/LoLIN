package com.lolin.model;

public class IconDto {
    private String nickName;
    private String iconUrl;
    public String getNickName() {
        return nickName;
    }
    public void setNickName(String nickName) {
        this.nickName = nickName;
    }
    public String getIconUrl() {
        return iconUrl;
    }
    public void setIconUrl(String iconUrl) {
        this.iconUrl = iconUrl;
    }
    @Override
    public String toString() {
        return "IconDto [nickName=" + nickName + ", iconUrl=" + iconUrl + "]";
    }
    
    
}