function validateForm() {
  let mapName = document.getElementById("map_name").value;
  let ctMoney = document.getElementById("ct_money").value;
  let tMoney = document.getElementById("t_money").value;
  let ctAlive = document.getElementById("ct_alive").value;
  let tAlive = document.getElementById("t_alive").value;
  let bombPlanted = document.getElementById("bomb_planted").value;

  if (!mapName) {
    alert("Map name is required");
    return false;
  }

  if (ctMoney <= 0 || tMoney <= 0) {
    alert("CT and T money must be positive numbers");
    return false;
  }

  if (ctAlive < 0 || tAlive < 0) {
    alert("Players alive must be zero or a positive number!!!");
    return false;
  }

  if (bombPlanted !== "0" && bombPlanted !== "1") {
    alert("Bomb planted must be either 0 or 1!!!!");
    return false;
  }

  // All validations passed
  return true;
}
