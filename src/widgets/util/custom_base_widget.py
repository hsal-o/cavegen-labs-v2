from abc import ABC, abstractmethod
import tkinter as tk

from util.create_tool_tip import CreateToolTip

class CustomBaseWidget(ABC):
    def __init__(self, type, tooltip=None):
        self.type = type
        if tooltip:
            CreateToolTip(self, tooltip)
        self._is_visible = True

    """Pack the widget"""
    def apply_pack(self, *args, **kwargs):
        self.pack(fill=tk.X, padx=8, pady=2)

    # Add Enable/Disable method for interactable widgets?

    """Show the widget"""
    def show(self):
        self.apply_pack()
        self._is_visible = True

    """Hide the widget"""
    def hide(self):
        self.pack_forget()
        self._is_visible = False

    """Method to check if widget is visible"""
    def is_visible(self):
        return self._is_visible

    """Get the widget's specified value type"""
    def get_type(self):
        return self.type

    """Wrapper method to ensure visibility check before checking if widget is empty
        - Wrapper is necessary as _evaluate_empty could be overridden by children,
          leading to potential loss of visibility check if no wrapper was in place."""
    def is_empty(self):
        if not self.is_visible():
            return False
        
        return self._evaluate_empty()

    """Generic method to grab a widget's value through the specified typing"""
    def get(self):
        # Retrieve the widget's value (could be single value or a tuple)
        raw_value = self._get_value()

        # If it's a tuple, process each value individually
        if isinstance(raw_value, tuple):
            return tuple(self._process_value(value) for value in raw_value)
        
        # Otherwise, process the single value
        return self._process_value(raw_value)
    
    """Internal method that processes valid values"""
    def _process_value(self, value):
        # Handle empty values (None or empty strings)
        if value is None or str(value).strip() == "":
            return None
        
        # Attempt to convert the value to the correct type
        try:
            return self.type(value)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid input for type {self.type.__name__}: {e}")

    ########################################
    # Overridable Methods
    ######################################## 
    """Internal method to check if a widget was left empty/unsanswered
        - Can be overriden for widgets with more complex logic"""
    def _evaluate_empty(self):
        value = self.get()
        if isinstance(value, tuple):
            return any(v is None for v in value)
        return value is None
    
    ########################################
    # Abstract Methods
    ######################################## 
    """Internal Abstract method for widgets to implement how the value will be extracted"""
    @abstractmethod
    def _get_value(self):
        """Return the widget's value, having converted it to the specified type"""
        pass

    """Abstract method for widgets to set their value(s)"""
    @abstractmethod
    def set(self, value):
        """Set the widget's value"""
        pass