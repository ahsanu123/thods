include("tanks.jl")

mutable struct FlexyTank <: Tank
  drymass::Float64
  totalmass::Float64
  propellant::Float64


  function FlexyTank(drymass::Number, totalmass::Number)
    new(drymass, totalmass, totalmass - drymass)
  end

end

drymass(tank::FlexyTank) = tank.drymass
totalmass(tank::FlexyTank) = tank.totalmass

